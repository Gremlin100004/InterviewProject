
changePositionElement();
changeHeight();
window.addEventListener('resize', changePositionElement);

function changePositionElement() {
  // let wd = (window.innerWidth / 2);
  let wd = (document.documentElement.clientWidth / 2);
  let menu_left = document.getElementById('navAccordion');
  let wd_cont = document.getElementById('content').clientWidth;
  menu_left.style.marginLeft = (wd - wd_cont/2 - 233) + "px";

}

function changeHeight() {
    let wd_content = document.getElementById('content');

    if (wd_content.clientHeight < 950){
      wd_content.style.height = 922 + "px";
    }
}
