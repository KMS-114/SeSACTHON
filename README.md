# SeSACTHON

### Node.js Install
Node.js
conda install nodejs

### Svelte Start
npm create vite@latest frontend -- --template svelte
cd frontend
npm install
npm install svelte-routing
npm install less less-loader --save-dev
npx lessc src/styles/login.less src/styles/styles.css
npm install bootstrap@5.3.3
npm run dev

### Fastapi Start
cmd
uvicorn main:app --reload