module.exports = {
  plugins: {
    "@tailwindcss/postcss": {},
    "postcss-simple-vars": {},
    "postcss-nested": {}
  },

  daisyui: {
    themes: [
        "light",
      {
        african: {
          primary: "#c084fc", // Un violet vibrant (peut-être inspiré de certains tissus)
          secondary: "#facc15", // Or, jaune riche
          accent: "#16a34a", // Vert luxuriant
          neutral: "#a855f7", // Autre nuance de violet
          "base-100": "#f5f5f5", // Gris clair, sable
          info: "#3abff8",
          success: "#84cc16",
          warning: "#fbbd23",
          error: "#f30d0d",

          "--rounded-box": "0.5rem",
          "--rounded-btn": "0.25rem",
          "--rounded-badge": "1.9rem",
          "--animation-btn": "0.25s",
          "--animation-input": ".2s ease",
          "--btn-text-case": "uppercase",
          "--btn-focus-scale": "0.95",
          "--border-btn": "1px",
          "--tab-border": "2px",
          "--tab-radius": "0.5rem",
        },
      },
    ],
},
}