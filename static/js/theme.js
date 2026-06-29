const themeBtn =
document.getElementById(
"theme-btn"
);

if(themeBtn){

themeBtn.addEventListener(
"click",
()=>{

document.body.classList.toggle(
"dark-mode"
);

});
}