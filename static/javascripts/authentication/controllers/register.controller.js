(function(){
	'use strict';

	angular
		.module('thinkster.authentication.controllers')
		.controller('RegisterController', RegisterController);

	RegisterController.$inject = ['$location', '$scope', 'Authentication'];

	function RegisterController($location, $scope, Authentication){
		var vm = this;

		vm.register = register;

		function register(){
			console.log('controller register fn');
			Authentication.register(vm.email, vm.password, vm.username);
		}
	}
})();