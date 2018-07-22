/* jshint esversion: 6*/

app = {};

app.init = function() {
    $('#add-task').click(() => {
        app.newTask();
    });
};

app.newTask = function() {
    $('#task-maker').addClass('displayed').removeClass('hidden');
};

$(document).ready(app.init);