const courses = ["25011510","22000140I"]   //此处需修改课程ID

function getRandomElement(arr) {
    if (!arr || arr.length === 0) {
        return null;
    }
    const randomIndex = Math.floor(Math.random() * arr.length);
    return arr[randomIndex];
}

function randomInterval() {
  return 500 + Math.random() * 1000; // 500~1500 毫秒之间
}

function loopClick() {
  const course = getRandomElement(courses);
  let buttonId = "button.cv-btn.cv-choice[data-number='" + course + "']" ;
  let btnSelect = document.querySelector(buttonId); 
  if (btnSelect) {
    btnSelect.click();
    console.log("尝试~");
  }

  let btnConfirm = document.querySelector("div.cv-sure.cvBtnFlag");
  if (btnConfirm) {
    btnConfirm.click();
  }

  setTimeout(loopClick, randomInterval());
}

loopClick();