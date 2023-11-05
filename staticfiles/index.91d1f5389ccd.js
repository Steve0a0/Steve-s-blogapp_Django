        const togglebtn = document.getElementsByClassName('.toggle-button')[0]
        const navlink = document.getElementsByClassName('.navbar .links')[0]
 
        togglebtn.addEventListener('click',()=>{
            if (navlink.style.display === 'none' || navlink.style.display === '') {
                navlink.style.display = 'block';
              } else {
                navlink.style.display = 'none';
              }
            });