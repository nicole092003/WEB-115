class person{
    constructor(fName,lName,Course,Role,sectionNumber) {
        this.fName = fName;
        this.lName = lName;
        this.Course = Course;
        this.Role = Role;
        this.sectionNumber = sectionNumber;  
    }
    show(){
        document.getElementById("output").innerHTML=
        this.fName + " " + this.lName + " has the role of "
        + this.Role + " in " + this.Course + " section "
        + this.sectionNumber + ".";
    }
    
};

function FirstName() {
    const input = document.getElementById("fName");
    const item = input.value;
    return item;
};

function LastName() {
    const input = document.getElementById("lName");
    const item = input.value;
    return item;
};

function Course() {
    const input = document.getElementById("Course");
    const item = input.value;
    return item;
};

function Role() {
    const input = document.getElementById("Role");
    const item = input.value;
    return item;
};

function sectionNumber() {
    const input = document.getElementById("sectionNumber");
    const item = input.value;
    return item;
};

function addPerson() {
    const visitor = new person(
        FirstName(),
        LastName(),
        Course(),
        Role(),
        sectionNumber()
    );
    visitor.show();
};

document.getElementById("add-person").addEventListener("click",addPerson);
document.getElementById("form-person").onsubmit = (e) => { e.preventDefault(); };


