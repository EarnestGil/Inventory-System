/** @type {import('tailwindcss').Config} */
const colors=require('tailwindcss/colors')
module.exports = {
  content: [
    '../../templates/**/*.html',
    './templates/base.html',
    '../templates/index.html',
    '../../templates/base.html',
    '../../users/templates/users/**/*.html',
    '../../stores/templates/stores/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        // you can either spread `colors` to apply all the colors
        ...colors,
        customColors:{
          100:'#CAF0F8',
          200:'#90E0EF',
          300:'#00B4D8',
          400:'#0077B6',
          500:'#03045E',
        },
        cWhite:{
          100:'#FDFDFD',
          200:'#FAF9F6',
          300:'#F0F8FF',

        }
        
        // or add them one by one and name whatever you want
        
      },
      fontFamily: {
        custom: ['Poppins', 'sans-serif'], // Use the Google font name
      },
      
    },
  },
  plugins: [
    
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/container-queries'),
    require('tailwindcss/colors'),
  ]
}


