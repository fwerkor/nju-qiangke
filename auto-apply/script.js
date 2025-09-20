(function() {
  console.log("⏳ 抢课脚本启动...");

  // 需要排除的课程号
  const excludedCourses = ["00202430", "00371620"];

  // 点击函数（带事件触发）
  function clickElement(el) {
    if (el) {
      el.click();
      console.log("✅ 点击：", el.outerText || el.getAttribute("data-number") || el.className);
    }
  }

  // 核心逻辑：刷新 -> 选课 -> 确认
  function tryGrab() {
    // 点击刷新按钮
    let refreshBtn = document.querySelector("button.cv-btn.refresh-btn");
    clickElement(refreshBtn);

    // 找到所有课程的“选择”按钮
    let choices = document.querySelectorAll("a.cv-choice[data-number]");
    for (let btn of choices) {
      let courseNum = btn.getAttribute("data-number");
      let isFull = btn.getAttribute("data-isfull");
      
      // 跳过已满/冲突/限制的 或者在排除列表里的
      if (isFull === "1" || excludedCourses.includes(courseNum)) continue;

      // 点击选课按钮
      clickElement(btn);

      // 点击两次确认按钮
        let confirmBtns = document.querySelectorAll("div.cv-sure.cvBtnFlag[data-type='sure'], div.cv-sure.cvBtnFlag:not([data-type])");
        setTimeout(() => {
      clickElement(confirmBtns[0]); // 第一次点击
      setTimeout(() => {
        clickElement(confirmBtns[1]); // 第二次点击
      }, 30); // 两次点击间隔 30ms
    }, 30); // 第一次点击前延迟 30ms

      break; // 一次只抢一门，抢完就跳出
    }
  }

  // 循环抢课（每 0.4 秒刷新一次）
  setInterval(tryGrab, 400);
})();