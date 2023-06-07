const groceries = ['milk', 'bread', 'eggs'];
ShowList();

function AddToList() {
    const input = document.getElementById("EnterItem");
    const item = input.value;
    
    input.value = '';
    groceries.unshift(item);
    
    ShowList();
}

function AddToListEnd() {
    const input = document.getElementById("EnterItem");
    const item = input.value;
    
    input.value = '';
    groceries.push(item);
    
    ShowList();
}

function DeleteFirstItem() {
    groceries.shift();

    ShowList();
}

function DeleteLastItem() {
    groceries.pop();

    ShowList();
}

function ShowList() {
    let list = "";

    for (let i = 0; i < groceries.length; i++){
        let item = groceries[i];
        list = list.concat("<li>").concat(item).concat("</li>");
    }
    
    document.getElementById("groceries").innerHTML = list;
}

document.getElementById("AddToList").addEventListener("click",AddToList);
document.getElementById("AddToListEnd").addEventListener("click",AddToListEnd);
document.getElementById("DeleteFirstItem").addEventListener("click", DeleteFirstItem);
document.getElementById("DeleteLastItem").addEventListener("click", DeleteLastItem);
document.getElementById("form-list").onsubmit = (e) => { e.preventDefault(); AddToList(); };