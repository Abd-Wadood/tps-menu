# The Pizza Shop

A simple, Apple-inspired static page for the original PDF menu, with download, Call and WhatsApp links for Barki Road and Bedian Road. All essential actions work without JavaScript. Subtle entry and press motion respects reduced-motion preferences.

## Run

Requires Node.js 20+.

- `npm run dev` — http://127.0.0.1:4173
- `npm run check` — verify local assets and contact destinations
- `npm run build` — generate `dist/`

## Cloudflare Pages

Framework: None. Build command: `npm run build`. Output directory: `dist`. No environment variables or backend needed. Deploy the repository or upload `dist/` using Cloudflare Pages. No production deployment has been created from this workspace.

## Edit

Replace `public/menus/original-menu.pdf` to update the PDF. Update the size/page label in `public/index.html` when replacing it. Edit branch contact links and addresses in that HTML file. The supplied original logo is compressed at `public/assets/logo.webp`. Styling is in `public/style.css`.

Contact numbers verified against the supplied PDF: Barki Road Call 0323 9091177 and WhatsApp 0301 8408177 (confirmed by the owner); Bedian Road Call and WhatsApp 0308 2566477. The PDF is fetched only when opened or downloaded.

The previous item-by-item menu has been replaced by the PDF landing page. There is no cart, search, category browsing or menu transcription in this version. System fonts, CSS motion and SVG icons keep it lightweight. No dedicated Apple UI/Motion skill was installed; the design uses those visual conventions directly.


## Six-page menu layout

View menu opens `public/menu.html`, which displays six locally hosted crops in a continuous column with equal widths and no gaps. Original proportions are retained, so the wider deals panel is shorter rather than stretched. Download PDF uses `public/menus/original-menu.pdf`, reordered to the exact same sequence: Order Now cover, Gen Xtra (Bedian flyer), Pizza, Smash Burgers, Lahori Chicken, Deals. The six-page PDF is approximately 3 MB. The original supplied file is preserved in Downloads.

`scripts/prepare-menu.py` crops the source brochure at its panel boundaries and produces the six images, manifest, thumbnail and PDF. Its input currently points to the original supplied PDF in Downloads. The PDF reuses original page content through clipping and transformations; it is not regenerated from lower-resolution screenshots. `public/menus/pages.json` records the sequence and image dimensions. If recropping, update the matching image dimensions in `public/menu.html`.

Verified all six rendered PDF pages visually, plus seamless image widths/no gaps/no horizontal overflow at 320, 390, 768 and 1440px. Screenshots: `screenshots/ordered-menu-*.png`.

The cover phone-number strip is removed from both the web image and downloadable PDF at the owner's request. The preparation script removes that horizontal band and closes the gap; the website's branch Call and WhatsApp buttons remain available.

## November 16 update

The menu now contains seven pages: Order Now, Gen Xtra, Pizza, Smash Burgers, Crispy Burgers, Lahori Chicken, Deals. The supplied 1647×912 Crispy Burgers PNG is inserted after page 4, kept at full native resolution in the viewer and embedded losslessly in the downloadable PDF. All pages retain a 600pt PDF width and equal viewer widths, with original aspect ratios and no gaps. The downloadable PDF is approximately 4.8 MB. The website logo is now the supplied red JPEG, cropped around the artwork and optimized as WebP. Earlier six-page notes describe the prior version.
