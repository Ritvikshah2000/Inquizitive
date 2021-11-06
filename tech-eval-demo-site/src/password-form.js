
export class PasswordForm {
  constructor() {
    this.password = '';
    this.strength = 0;
  }

  updateRequirements(){
    this.strength = 0;

    if (hasUpper(this.password)){
      document.getElementById("caps").style.color = "green"
      this.strength++
    }
    else{
      document.getElementById("caps").style.color = "red"
    }

    if (hasLower(this.password)){
      document.getElementById("lower").style.color = "green"
      this.strength++
    }
    else{
      document.getElementById("lower").style.color = "red"
    }

    if (hasNumber(this.password)){
      document.getElementById("number").style.color = "green"
      this.strength++
    }
    else{
      document.getElementById("number").style.color = "red"
    }

    if (this.password.length > 8){
      document.getElementById("len").style.color = "green"
      this.strength++
    }
    else{
      document.getElementById("len").style.color = "red"
    }

  
    document.getElementById("password-strength-meter").value = this.strength;
  }

}

function hasUpper(str) {

  for (let i = 0; i < str.length; i++) {
    if (!isNaN(str[i] * 1)) {
      continue
    }
    else {
      if (str[i] == str[i].toUpperCase()){
        return true
      }
    }
  }

  return false
}

function hasLower(str) {

  for (let i = 0; i < str.length; i++) {
    if (!isNaN(str[i] * 1)) {
      continue
    }
    else {
      if (str[i] == str[i].toLowerCase()){
        return true
      }
    }
  }

  return false
}

function hasNumber(str) {

  for (let i = 0; i < str.length; i++) {
    if (!isNaN(str[i] * 1)) {
      return true
    }
  }

  return false
}