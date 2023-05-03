const searchInput = document.getElementById("searchInput");
const search = document.getElementById("searchBar");

function search() {
  const searchTerm = document.getElementById("searchInput").value;
  window.location.href = "result.html";
}

document.addEventListener("DOMContentLoaded", function () {
  window.addEventListener("scroll", function () {
    if (window.scrollY > 200) {
      document.querySelector(".scroll-arrow").classList.add("show");
    } else {
      document.querySelector(".scroll-arrow").classList.remove("show");
    }
  });
});
