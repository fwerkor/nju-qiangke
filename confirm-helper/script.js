function loopClick() {
  let btnConfirm = document.querySelector("div.cv-sure.cvBtnFlag");
  if (btnConfirm) {
    btnConfirm.click();
    console.log("操作~");
  }

  setTimeout(loopClick, 200);
}

loopClick();