window.addEventListener("DOMContentLoaded", () => {
    const socket = io();

    // Lorsqu'on coche ou décoche une note
    document.querySelectorAll("input[type='checkbox']").forEach(checkbox => {
        checkbox.addEventListener("change", () => {
            const id = checkbox.dataset.id;
            const done = checkbox.checked;

            // On envoie la mise à jour à l'API
            fetch(`/api/notes/${id}`, {
                method: "PATCH",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ done })
            });
        });
    });

    // Lorsqu'on reçoit une mise à jour depuis le serveur
    socket.on("note_update", data => {
        // Recharger la page pour refléter les changements
        location.reload();
    });
});
