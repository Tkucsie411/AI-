// 追蹤選中按鈕的計數
let selectedCount = 0;

// 切換選中狀態的函數
function toggleSelection(button) {
  if (button.classList.contains("selected")) {
    button.classList.remove("selected");
    selectedCount--; // 減少選中數
  } else {
    button.classList.add("selected");
    selectedCount++; // 增加選中數
  }
}
function goBack() {
  window.history.back(); // 返回上一頁
}
// 跳轉到 page3
function goToPage3() {
  if (selectedCount > 0) {
    window.location.href = "/page3"; // 跳轉到 page3.html
  } else {
    alert("請至少選擇一個選項！");
  }
}
