import os
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image

from image_processor import process_image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("A4 Grid Print Automator")
        self.geometry("680x480")
        self.resizable(False,False)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.current_image_path=None
        self.final_canvas=None

        self.copy_count_values=["2","4","6","8"]
        
        self.setup_ui()

    def setup_ui(self):

        self.frame_left=ctk.CTkFrame(self,fg_color="transparent")
        self.frame_left.pack(side="left",padx=20,pady=20,fill="both",expand=True)

        self.frame_left.grid_columnconfigure(0,weight=1)
        self.frame_left.grid_columnconfigure(1,weight=1)

        self.frame_right=ctk.CTkFrame(self,fg_color=("#bebebe","gray15"),width=320,height=480)
        self.frame_right.pack(side="right",padx=20,pady=20)
        self.frame_right.pack_propagate(False)

        self.config_label=ctk.CTkLabel(self.frame_left,text="Layout Configuration",font=("Arial",22,"bold"))
        self.config_label.grid(row=0,column=0,columnspan=2)

        self.button_load_image=ctk.CTkButton(self.frame_left,text="Load new image",font=("Arial",13,"bold"),height=40,command=self.load_new_image)
        self.button_load_image.grid(row=1,column=0,columnspan=2,pady=30)

        self.label_choose_copy_count=ctk.CTkLabel(self.frame_left,text="Copies:",font=("Arial",20,"bold"))
        self.label_choose_copy_count.grid(row=2,column=0,sticky="w")

        self.combobox_choose_copy_count=ctk.CTkComboBox(self.frame_left,values=self.copy_count_values,command=self.render_preview,state="readonly")
        self.combobox_choose_copy_count.set("2")
        self.combobox_choose_copy_count.grid(row=2,column=1,sticky="e")

        self.checkbox_rotate=ctk.CTkCheckBox(self.frame_left,text="Rotate original image 90°",command=self.render_preview)
        self.checkbox_rotate.grid(row=3,column=0,columnspan=2,sticky="w",pady=30)

        self.checkbox_grayscale=ctk.CTkCheckBox(self.frame_left,text="Grayscale",command=self.render_preview)
        self.checkbox_grayscale.grid(row=4,column=0,columnspan=2,sticky="w")

        self.checkbox_guidelines=ctk.CTkCheckBox(self.frame_left,text="Show cut guidelines",command=self.render_preview)
        self.checkbox_guidelines.grid(row=5,column=0,columnspan=2,sticky="w",pady=30)

        self.button_save_file=ctk.CTkButton(self.frame_left,text="Save File",width=120,state="disabled",command=self.save_file)
        self.button_save_file.grid(row=6,column=0,pady=62,sticky="w")

        self.button_print=ctk.CTkButton(self.frame_left,text="Print",width=120,state="disabled",command=self.print_image)
        self.button_print.grid(row=6,column=1,pady=62,sticky="e")

        self.label_preview=ctk.CTkLabel(self.frame_right,text="No image currently loaded",fg_color=("#cfcfcf","gray20"),text_color=("#000000","#ffffff"),width=280,height=396,corner_radius=0)
        self.label_preview.pack(expand=True)

    def render_preview(self,*args):
        
        if not self.current_image_path:
            return
        
        try:
                        
            copies=int(self.combobox_choose_copy_count.get())
            rotate=bool(self.checkbox_rotate.get())
            grayscale=bool(self.checkbox_grayscale.get())
            guidelines=bool(self.checkbox_guidelines.get())
            
            self.final_canvas=process_image(self.current_image_path,copies,rotate,guidelines)

            if grayscale:
                self.final_canvas=self.final_canvas.convert("L")
                self.final_canvas=self.final_canvas.convert("RGB")

            preview_w,preview_h=280,396
            canvas_preview=self.final_canvas.resize((preview_w,preview_h),Image.Resampling.LANCZOS)

            gui_preview_canvas=ctk.CTkImage(light_image=canvas_preview,dark_image=canvas_preview,size=(preview_w,preview_h))

            self.label_preview.configure(image=gui_preview_canvas,text="")

            self.button_save_file.configure(state="normal")
            self.button_print.configure(state="normal")

        except Exception as e:
            
            self.label_preview.configure(image=None,text="Error: File cannot\nbe processed!")

            self.button_save_file.configure(state="disabled")
            self.button_print.configure(state="disabled")

    def load_new_image(self):
        path=filedialog.askopenfilename(title="Open Image",filetypes=[("Images","*.png *.jpg *.jpeg *.webp *.jfif")])
        if path:
            self.current_image_path=path
            self.render_preview()

    def save_file(self):
        if self.final_canvas:
            save_path=filedialog.asksaveasfilename(title="Save As",defaultextension=".pdf",filetypes=[("Document PDF (*.pdf)","*.pdf"),("Image PNG (*.png)","*.png"),("Image JPG (*.jpg)","*.jpg")])
            if save_path:
                _,extension=os.path.splitext(save_path.lower())
                if extension==".pdf":
                    self.final_canvas.save(save_path,"PDF",resolution=300.0)
                else:
                    self.final_canvas.save(save_path)

    def print_image(self):
        if self.final_canvas:
            temp_path="temp_print_file.pdf"
            self.final_canvas.save(temp_path,"PDF",resolution=300.0)
            try:
                os.startfile(temp_path)
            except Exception as e:
                pass

if __name__=="__main__":
    app=App()
    app.mainloop()
