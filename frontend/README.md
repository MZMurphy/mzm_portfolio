# sv

Everything you need to build a Svelte project, powered by [`sv`](https://github.com/sveltejs/cli).

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```sh
# create a new project
npx sv create my-app
```

To recreate this project with the same configuration:

```sh
# recreate this project
npx sv create --template minimal --types ts --add prettier eslint tailwindcss="plugins:typography" --install npm frontend
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```sh
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```sh
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.

# MZM_PORTFOLIO // Quant Platform Engineer

Personal portfolio for Mariesha Zara Murphy, built to bridge the gap between low-level systems engineering and high-performance web architecture.

## ⚡ Tech Stack
- **Framework:** SvelteKit (Svelte 5)
- **Styling:** Tailwind CSS v4.0 (OLED/Dark Mode Theme)
- **Language:** TypeScript
- **Fonts:** Inter (UI) + JetBrains Mono (Code/Terminal elements)

## 🛠️ System Status (Completed)
- [x] **Core Architecture:** SvelteKit + Vite + Tailwind v4 integration.
- [x] **OLED Theme:** Custom deep navy (`#020617`) background with high-contrast text.
- [x] **Typography Engine:** configured `layout.css` to load Google Fonts with fallback variables.
- [x] **Layout Systems:**
    - **Hero:** Sticky glassmorphism navigation + "Command Center" header.
    - **Projects:** 3-Column CSS Grid with video placeholder slots.
    - **Experience:** Vertical timeline audit log style.
- [x] **Assets:** CSS-only glass panels, terminal bars, and status badges.

## 🚀 Next Steps / Roadmap
- [ ] **Media Pipeline:** Replace `.webm` placeholders with actual project demos.
- [ ] **Interactivity:** Wire up the "Contact" form/mailto actions.
- [ ] **Mobile Optimization:** Fine-tune grid collapse for mobile devices.
- [ ] **Deployment:** Push to Vercel/Netlify.

## 📦 Setup
```bash
npm install
npm run dev