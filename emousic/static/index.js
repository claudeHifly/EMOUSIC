$(document).ready(function () {
    $("#main_row").css("padding-top", $("#title_navbar").height());
    $("#loading_analysis").css("display", "none");

    $("#form_load").submit(function (e) {
        $("#start_analysis").css("display", "none");
        $("#loading_analysis").css("display", "inline");
    });

    $("#form_load").change(function (e) {
        console.log("changed");
    });

    $('input[type="file"]').change(function (e) {
        var reader = new FileReader();

        // read the image file as a data URL.
        reader.readAsDataURL(this.files[0]);

        var fileName = e.target.files[0].name;
        // alert('The file "' + fileName +  '" has been selected.');
    });

    $("#player").css("height", $("#start_analysis").css("height"));

});