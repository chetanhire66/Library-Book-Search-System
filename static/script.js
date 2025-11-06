// static/script.js
// Minimal client-side helpers (can expand as needed)

document.addEventListener("DOMContentLoaded", function () {
    // Example: confirm before delete (progressive enhancement)
    const deleteForm = document.getElementById("deleteForm");
    if (deleteForm) {
      deleteForm.addEventListener("submit", function (e) {
        const confirmed = confirm("Are you sure you want to delete this book?");
        if (!confirmed) e.preventDefault();
      });
    }
  });