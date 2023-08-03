const taskForm = document.getElementById("task-form");
const taskList = document.getElementById("task-list");

document.addEventListener("DOMContentLoaded", () => {
    const editButtons = document.querySelectorAll(".edit-btn");
    const deleteButtons = document.querySelectorAll(".delete-btn");

    editButtons.forEach(button => {
        button.addEventListener("click", () => {
            const taskId = button.getAttribute("data-id");
            // You can use taskId to identify the task and perform an edit action
            // For example, redirect to an edit page or open a modal for editing
        });
    });

    deleteButtons.forEach(button => {
        button.addEventListener("click", () => {
            const taskId = button.getAttribute("data-id");
            if (confirm("Are you sure you want to delete this task?")) {
                // Perform the delete action using AJAX or a form submission
                // You will need to send the taskId to the server for deletion
                // After successful deletion, you can remove the task from the DOM
            }
        });
    });

    const taskForm = document.getElementById("task-form");
    const taskList = document.getElementById("task-list");

    taskForm.addEventListener("submit", (e) => {
        e.preventDefault();

        const taskName = document.getElementById("task-name").value;
        const taskDescription = document.getElementById("task-description").value;

        if (taskName && taskDescription) {
            const taskDiv = document.createElement("div");
            taskDiv.classList.add("task");
            taskDiv.innerHTML = `
                <h3>${taskName}</h3>
                <p>${taskDescription}</p>
            `;

            taskList.appendChild(taskDiv);

            document.getElementById("task-name").value = "";
            document.getElementById("task-description").value = "";
        }
    });
});

