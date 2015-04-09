(function(){
	'use strict';
	angular
		.module('thinkster.routes')
		.config(config);

	config.$inject = ['$routeProvider'];

	function config($routeProvider){
		$routeProvider.when('/register', {
			controller: 'RegisterController',
			// refer to controller as 'vm' in template
			controllerAs: 'vm',
			templateUrl: '/static/templates/authentication/register.html'
		}).otherwise('/');
	}
})();