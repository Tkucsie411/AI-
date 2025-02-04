

// page2.js

document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".interest-button");
  const submitBtn = document.querySelector(".submit-btn");
  const selectedInterests = new Set();

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      button.style.backgroundColor = selectedInterests.has(button.textContent) 
        ? "#007bff" // Deselect
        : "#0056b3"; // Select
      selectedInterests[selectedInterests.has(button.textContent) ? "delete" : "add"](button.textContent);
    });
  });

  submitBtn.addEventListener("click", () => {
    selectedInterests.size < 2 
      ? alert("請選擇至少兩個職業！") 
      : window.location.href = "/page3";
  });
});
