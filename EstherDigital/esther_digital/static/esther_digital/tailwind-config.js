tailwind.config = {
  theme: { extend: {
    colors: {
      page:  'oklch(0.97203762 0.02147374 130.00721861)',
      sand:  'oklch(0.94784964 0.02814844 86.64564754)',
      brand: 'oklch(0.66399775 0.16354272 133.98188886)',
      moss:  'oklch(0.64863024 0.06475043 129.64934722)',
      line:  'oklch(0.89457293 0.00437622 17.23921485)',
      field: 'oklch(0.86466520 0.00552345 17.26386497)'
    },
    fontFamily: { serif: ['Newsreader', 'Georgia', 'serif'] },
    boxShadow: { card: '0 5px 7px oklch(0 0 0 / .25)', form: '0 5px 16px oklch(0 0 0 / .25)' }
  } }
};
