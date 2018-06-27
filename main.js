app = {};

app.init = function() {
    $('button #add-task').click(() => {
        app.newTask();
    });
};

app.newTask = function() {
    
};

$(app.init);