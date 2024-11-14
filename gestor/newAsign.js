function newUserAsign() {
    console.log("newUserAsign");
    const modal = document.getElementById("add-new-user-form");
    if (modal.style.display === "flex") {
        modal.style.display = "none";
        document.body.style.overflow = "auto"; 
    } else {
        modal.style.display = "flex";
        document.body.style.overflow = "hidden"; 
    }
}

document.getElementById("add-new-user-form").addEventListener("click", function(event) {
    const modalContent = document.querySelector(".form-new-user");
    if (!modalContent.contains(event.target)) {
        newUserAsign();
    }
});