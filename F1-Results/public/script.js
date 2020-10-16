var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        proccessData(this.responseXML);
    }
};
xhttp.open("GET", "http://ergast.com/api/f1/current/driverStandings", true);
xhttp.send();
function proccessData(xml){
    var season_round=[xml.getElementsByTagName("StandingsList")[0].attributes.season.value,xml.getElementsByTagName("StandingsList")[0].attributes.round.value] ;
    var arr= xml.getElementsByTagName("StandingsList")[0].children;
    console.log(arr)
    var tablebody= $("table tbody");
    $("table caption").append(season_round[0]+" Season - Round "+season_round[1]);

    for (const result of arr) {
        tablebody.append("<tr>");
            var position = result.attributes[0].value;
            var points = result.attributes[2].value;
            var pilot = result.getElementsByTagName("Driver");
            pilot = pilot[0].children[1].innerHTML + " " + pilot[0].children[2].innerHTML;
            var team = result.getElementsByTagName("Constructor");
            team = team[0].children[0].innerHTML
            tablebody.append("<td >"+position+"</td>");
            tablebody.append("<td >"+pilot+"</td>");
            tablebody.append("<td >"+team+"</td>");
            tablebody.append("<td >"+points+"</td>");
        tablebody.append("</tr>")
    }
}