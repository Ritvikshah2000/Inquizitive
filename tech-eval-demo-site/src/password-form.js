import { observable } from "../node_modules/aurelia-binding/dist/aurelia-binding";

export class PasswordForm {
  constructor() {
    this.password = '';
    this.strength = 0;
    this.hasCaps = false;
    this.hasLower = false;
    this.hasSymbols = false;
    this.passLength = false;
  }
}


document.getElementById('inputBar').getElementById('passInput').oninput = function() {updateRequirements()};

function updateRequirements(){
  //if this.password
  alert("The value of the input field was changed.");
  //document.getElementById("caps").innerText.fontcolor = "green"
  //this.strength = this.strength + 1

  //document.getElementById("password-strength-meter").value = "2";
}
