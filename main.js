/* jshint esversion: 6*/

app = {};

app.init = function() {
    document.getElementById('add-task').addEventListener('click', app.newTask);
};

app.newTask = function() {
//    $('#task-maker').addClass('displayed').removeClass('hidden');
    document.getElementById('task-maker').className = 'displayed';

    document.querySelector('#task-maker > form > button.submit').addEventListener('click', (e) => {
        e.preventDefault();
        console.log('Submit button clicked');
    });

    document.getElementById('task-maker').className = 'hidden';
};

document.addEventListener("DOMContentLoaded", app.init);