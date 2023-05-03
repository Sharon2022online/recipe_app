let ingredientCount = 1;

function addIngredient() {
  ingredientCount++;

  const ingredientsDiv = document.getElementById("ingredients");

  const ingredientDiv = document.createElement("div");
  ingredientDiv.classList.add("ingredient", "form-row");

  const nameDiv = document.createElement("div");
  nameDiv.classList.add("col");

  const nameInput = document.createElement("input");
  nameInput.type = "text";
  nameInput.classList.add("form-control");
  nameInput.id = `ingredient-name-${ingredientCount}`;
  nameInput.name = `ingredient-name-${ingredientCount}`;
  nameInput.placeholder = "Ingredient Name";
  nameInput.required = true;

  nameDiv.appendChild(nameInput);
  ingredientDiv.appendChild(nameDiv);

  const quantityDiv = document.createElement("div");
  quantityDiv.classList.add("col");

  const quantityInput = document.createElement("input");
  quantityInput.type = "number";
  quantityInput.classList.add("form-control");
  quantityInput.id = `ingredient-quantity-${ingredientCount}`;
  quantityInput.name = `ingredient-quantity-${ingredientCount}`;
  quantityInput.placeholder = "Quantity";
  quantityInput.required = true;

  quantityDiv.appendChild(quantityInput);
  ingredientDiv.appendChild(quantityDiv);

  const unitDiv = document.createElement("div");
  unitDiv.classList.add("col");

  const unitSelect = document.createElement("select");
  unitSelect.classList.add("form-control");
  unitSelect.id = `ingredient-unit-${ingredientCount}`;
  unitSelect.name = `ingredient-unit-${ingredientCount}`;

  const noneOption = document.createElement("option");
  noneOption.value = "none";
  noneOption.disabled = true;
  noneOption.selected = true;
  noneOption.textContent = "Select Unit";

  const gramsOption = document.createElement("option");
  gramsOption.value = "grams";
  gramsOption.textContent = "grams";

  const millilitersOption = document.createElement("option");
  millilitersOption.value = "milliliters";
  millilitersOption.textContent = "milliliters";

  const teaspoonsOption = document.createElement("option");
  teaspoonsOption.value = "teaspoons";
  teaspoonsOption.textContent = "teaspoons";

  const tablespoonsOption = document.createElement("option");
  tablespoonsOption.value = "tablespoons";
  tablespoonsOption.textContent = "tablespoons";

  unitSelect.appendChild(noneOption);
  unitSelect.appendChild(gramsOption);
  unitSelect.appendChild(millilitersOption);
  unitSelect.appendChild(teaspoonsOption);
  unitSelect.appendChild(tablespoonsOption);

  unitDiv.appendChild(unitSelect);
  ingredientDiv.appendChild(unitDiv);

  ingredientsDiv.appendChild(ingredientDiv);
}

function removeIngredient() {
  const ingredientsDiv = document.getElementById("ingredients");
  const ingredients = ingredientsDiv.getElementsByClassName("ingredient");
  if (ingredients.length > 1) {
    ingredients[ingredients.length - 1].remove();
    ingredientCount--;
  }
}
