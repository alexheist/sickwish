var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
var values = {
  name: "",
  email: "",
  message: "",
  csrfmiddlewaretoken: csrfToken
};

function handleFocus(id) {
  var field = document.getElementById(id);
  field.classList.add("form__field--active");
}

function handleBlur(id) {
  var field = document.getElementById(id);
  if (values[field.id] === "") {
    field.classList.remove("form__field--active");
  }
}

function handleChange(field) {
  values[field.name] = field.value;
}
