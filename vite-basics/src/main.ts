import './style.css';


interface Task {
  id: number;
  text: string;
  completed: boolean;
}

const taskForm = document.querySelector<HTMLFormElement>('#task-form')!;
const taskInput = document.querySelector<HTMLInputElement>('#task-input')!;
const taskList = document.querySelector<HTMLUListElement>('#task-list')!;

let tasks: Task[] = [];

// Agregar una tarea
const addTask = (text: string): void => {
  const newTask: Task = {
    id: Date.now(),
    text,
    completed: false,
  };
  tasks.push(newTask);
  renderTasks();
};

// Renderizar las tareas
const renderTasks = (): void => {
  taskList.innerHTML = '';
  tasks.forEach((task) => {
    const li = document.createElement('li');
    li.textContent = task.text;

    // Botón para eliminar
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Eliminar';
    deleteButton.onclick = () => {
      tasks = tasks.filter((t) => t.id !== task.id);
      renderTasks();
    };

    li.appendChild(deleteButton);
    taskList.appendChild(li);
  });
};

// Manejar el envío del formulario
taskForm.onsubmit = (e) => {
  e.preventDefault();
  if (taskInput.value.trim()) {
    addTask(taskInput.value.trim());
    taskInput.value = '';
  }
};
