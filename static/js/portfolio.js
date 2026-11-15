(function () {
    "use strict";

    // Project dialogs
    document.querySelectorAll(".project-details-btn").forEach(function (btn) {
        btn.addEventListener("click", function () {
            var dialog = document.getElementById(btn.dataset.dialog);
            if (dialog && typeof dialog.showModal === "function") dialog.showModal();
        });
    });
    document.querySelectorAll(".project-dialog").forEach(function (dialog) {
        // Click on the backdrop closes the dialog
        dialog.addEventListener("click", function (e) {
            if (e.target === dialog) dialog.close();
        });
    });

    // Project filters
    var buttons = document.querySelectorAll(".filter-btn");
    var cards = document.querySelectorAll(".project-card");
    buttons.forEach(function (btn) {
        btn.addEventListener("click", function () {
            var filter = btn.dataset.filter;
            buttons.forEach(function (b) { b.classList.toggle("active", b === btn); });
            cards.forEach(function (card) {
                card.hidden = !(filter === "all" || card.dataset.category === filter);
            });
        });
    });

    // Auto-dismiss toast messages
    var toasts = document.querySelectorAll(".contact-toast");
    if (toasts.length) {
        setTimeout(function () {
            toasts.forEach(function (t) { t.style.transition = "opacity .5s"; t.style.opacity = "0"; });
            setTimeout(function () { toasts.forEach(function (t) { t.remove(); }); }, 600);
        }, 6000);
    }
})();
