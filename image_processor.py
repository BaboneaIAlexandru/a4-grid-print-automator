import os
from PIL import Image,ImageOps,ImageDraw

def process_image(image_path,copy_count,rotate,show_guidelines):
    
    img=Image.open(image_path)

    img=ImageOps.exif_transpose(img)

    if img.mode!="RGB":
        img=img.convert("RGB")

    if rotate:
        img=img.rotate(90,expand=True)
    
    img_w,img_h=img.size
    
    a4_w=2480
    a4_h=3508

    if copy_count==2:
        limit_w=a4_w
        limit_h=a4_h//2
    elif copy_count==4:
        limit_w=a4_w//2
        limit_h=a4_h//2
    elif copy_count==6:
        limit_w=a4_w//2
        limit_h=a4_h//3
    elif copy_count==8:
        limit_w=a4_w//2
        limit_h=a4_h//4

    w_ratio=limit_w/img_w
    h_ratio=limit_h/img_h

    scale_factor=min(w_ratio,h_ratio)

    img_w=int(img_w*scale_factor)
    img_h=int(img_h*scale_factor)
    img=img.resize((img_w,img_h),Image.Resampling.LANCZOS)

    canvas=Image.new("RGB",(a4_w,a4_h),"white")

    empty_x=(limit_w-img_w)//2
    empty_y=(limit_h-img_h)//2

    if copy_count==2:
        rows,columns=2,1
    elif copy_count==4:
        rows,columns=2,2
    elif copy_count==6:
        rows,columns=3,2
    elif copy_count==8:
        rows,columns=4,2

    for row in range(rows):
        for column in range(columns):
            
            x_pos=(column*limit_w)+empty_x
            y_pos=(row*limit_h)+empty_y

            canvas.paste(img,(x_pos,y_pos))
    
    if show_guidelines:

        draw=ImageDraw.Draw(canvas)
        guideline_color="#848484"
        guideline_w=3

        for column in range(1,columns):
            x=column*limit_w
            draw.line([(x,0),(x,a4_h)],fill=guideline_color,width=guideline_w)
        
        for row in range(1,rows):
            y=row*limit_h
            draw.line([(0,y),(a4_w,y)],fill=guideline_color,width=guideline_w)

    return canvas
