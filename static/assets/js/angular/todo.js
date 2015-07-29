

    function TodoCtrl($scope) {
    $scope.todos = [
    {text:'Assignement 1 HCI (DeadLine: 2days)', done:true},
    {text:'Lab 4 HCI (Completed)', done:true},
    {text:'Mini Project HCI remaining..', done:false}];
     
    $scope.addTodo = function() {
    $scope.todos.push({text:$scope.todoText, done:false});
    $scope.todoText = '';
    };
     
    $scope.remaining = function() {
    var count = 0;
    angular.forEach($scope.todos, function(todo) {
    count += todo.done ? 0 : 1;
    });
    return count;
    };
     
    $scope.archive = function() {
    var oldTodos = $scope.todos;
    $scope.todos = [];
    angular.forEach(oldTodos, function(todo) {
    if (!todo.done) $scope.todos.push(todo);
    });
    };
    }

