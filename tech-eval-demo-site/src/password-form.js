
export class PasswordForm {
  constructor() {
    this.password = '';
    this.strength = 0;
    this.barColor = 'red'
    this.strenghtText = '';
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

    //bar = document.getElementById("password-strength-meter")
    //bar.value = this.strength;

    document.getElementById("password-strength-meter").value = this.strength;

    switch(this.strength) {
      case 0:
        this.strenghtText = '';
        break;
      case 1:
        this.strenghtText = 'terrible';
        break;

      case 2:
        this.strenghtText = 'weak';
        break;

      case 3:
        this.strenghtText = 'medium';
        break;
       
      case 4:
        this.strenghtText = 'strong';
        break;

      default:
        this.strenghtText = '';
    }
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