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

