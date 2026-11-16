from pypdf import PdfReader, PdfWriter, Transformation, PageObject
from pypdf.generic import RectangleObject
from PIL import Image
from pathlib import Path
from copy import copy
import shutil,json,subprocess
from io import BytesIO
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
source=Path(r'C:\Users\wadoo\Downloads\Pizza_Shop_All_Menus.pdf')
r=PdfReader(source)
out=Path('public/menus/pages');out.mkdir(parents=True,exist_ok=True)
Path('output/pdf').mkdir(parents=True,exist_ok=True)
# Brochure folds; the owner requested removal of the cover's phone strip.
sections=[('Order Now',2,1365,2048),('Gen Xtra',0,0,1234),('Pizza',1,0,692),('Smash Burgers',1,692,1364),('Lahori Chicken',1,1364,2048),('Deals',2,0,1365)]
w=PdfWriter();manifest=[]
for idx,(label,page_index,x0,x1) in enumerate(sections,1):
    source_page=r.pages[page_index]
    image=list(source_page.images)[0].image.convert('RGB')
    iw,ih=image.size
    crop=image.crop((x0,0,x1,ih))
    page_number=len(manifest)+1
    name=f'{page_number:02d}.jpg'
    crop.save(out/name,quality=93,subsampling=0,optimize=True)
    pw=float(source_page.mediabox.width);ph=float(source_page.mediabox.height)
    left=x0/iw*pw;right=x1/iw*pw;scale=600/(right-left)
    clipped=copy(source_page);clipped.cropbox=RectangleObject((left,0,right,ph))
    if idx==1:
        # Remove source-image rows 780:855, closing the gap without masking text.
        unit=ph/ih
        removed=75*unit
        dest=PageObject.create_blank_page(width=600,height=(ph-removed)*scale)
        upper=copy(source_page)
        upper.cropbox=RectangleObject((left,ph-780*unit,right,ph))
        dest.merge_transformed_page(upper,Transformation().translate(-left,-removed).scale(scale))
        lower=copy(source_page)
        lower.cropbox=RectangleObject((left,0,right,ph-855*unit))
        dest.merge_transformed_page(lower,Transformation().translate(-left,0).scale(scale))
    else:
        dest=PageObject.create_blank_page(width=600,height=ph*scale)
        dest.merge_transformed_page(clipped,Transformation().translate(-left,0).scale(scale))
    w.add_page(dest)
    manifest.append(dict(page=page_number,title=label,width=crop.width,height=crop.height-(75 if idx==1 else 0),src='menus/pages/'+name))
    if idx==4:
        # Embed supplied artwork at its full native resolution, without resampling.
        artwork=Path('public/menus/source/crispy-burgers.png')
        with Image.open(artwork) as added:
            aw,ah=added.size
        height=600*ah/aw
        buffer=BytesIO()
        canvas=Canvas(buffer,pagesize=(600,height))
        canvas.drawImage(ImageReader(str(artwork)),0,0,width=600,height=height)
        canvas.showPage();canvas.save();buffer.seek(0)
        w.add_page(PdfReader(buffer).pages[0])
        shutil.copyfile(artwork,out/'05.png')
        manifest.append(dict(page=5,title='Crispy Burgers',width=aw,height=ah,src='menus/pages/05.png'))
w.add_metadata({'/Title':'The Pizza Shop Menu','/Author':'The Pizza Shop'})
w.write('output/pdf/The-Pizza-Shop-Menu.pdf')
shutil.copyfile('output/pdf/The-Pizza-Shop-Menu.pdf','public/menus/original-menu.pdf')
# Render the edited PDF cover for the web viewer, so both use the same artwork.
subprocess.run(['pdftoppm','-f','1','-l','1','-singlefile','-scale-to-x','683','-scale-to-y','964','-jpeg','-jpegopt','quality=93','public/menus/original-menu.pdf','public/menus/pages/01'],check=True)
thumb=Image.open('public/menus/pages/01.jpg');thumb.thumbnail((180,254));thumb.save('public/assets/menu-preview.webp',quality=88)
Path('public/menus/pages.json').write_text(json.dumps(manifest,indent=2))
check=PdfReader('public/menus/original-menu.pdf');assert len(check.pages)==7
assert all(abs(float(p.mediabox.width)-600)<.01 for p in check.pages)
print(json.dumps(manifest,indent=2));print('PDF bytes',Path('public/menus/original-menu.pdf').stat().st_size)
