<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@page language="java" session="true" %>
<%@page import = "java.sql.*" import = "com.ProjectController.*" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta name="description" content="" />
<meta name="keywords" content="" />
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<link REL="icon" href="http://www.baruch.cuny.edu/favicon.ico">
<link rel="stylesheet" type="text/css" href="baruch_interior.css" />
<link rel="stylesheet" type="text/css" href="http://www.baruch.cuny.edu/css/application.css" />
<link href="scheduler.css" rel="stylesheet" type="text/css" />
<%//Use scriptlet to handle query execution

//Create and initialize variables for the query, controller class, and search result
String query = null; ProjectDAC resultDAC = new ProjectDAC(); ResultSet result = null; String resID = null;

//Get the bean from the session
ProjectBean mySearch = (ProjectBean) session.getAttribute("searchBean");
query = resultDAC.buildSearch(mySearch.getSemester(), mySearch.getDepartment(), mySearch.getDiscipline(), mySearch.getdivision(), mySearch.getcNumber(), mySearch.getDays(), mySearch.getTimeAB(), mySearch.getTime(), mySearch.getInstructor());            
result = resultDAC.runQuery(query);%>

<title>Results</title>
</head>
<body>
<div id="wrapper">
<div id="banner"><a href="http://www.baruch.cuny.edu"><img src="http://www.baruch.cuny.edu/images/logo_baruch.gif" alt="Baruch College" name="logo" width="201" height="68" border="0" id="logo" /></a></div>
<div id="main">
<div>
<p>Search results are based on the following keywords:</p>
  <table id="criteria" summary="This table contains the search criteria. Results are listed in next table.">
    <tr>
      <td><strong>Semester</strong>: ${searchBean.semester}</td>
      <td><strong>Days</strong>: ${searchBean.days}</td>
    </tr>
    <tr>
      <td><strong>Department</strong>: ${searchBean.department}</td>
      <td><strong>Time</strong>: ${searchBean.timeAB} ${searchBean.time}</td>
    </tr>
    <tr>
      <td><strong>Discipline</strong>: ${searchBean.discipline}</td>
      <td><strong>Course number</strong>: ${searchBean.cNumber}</td>
    </tr>
    <tr>
      <td><strong>Division</strong>: ${searchBean.uG}</td>
      <td><strong>Instructor</strong>: ${searchBean.instructor} </td>
    </tr>
    </table>
  <font color="red">
	  <p><b>The schedule was LAST&nbsp; updated at 9:00am on Nov 27th, 2006.</b></p>
	  <p>Due to the dynamic nature of the registration process, not all courses listed as open will have space for new registrants.</p>
  </font>
  </div>
<form method="post" action="controlServlet">
<table id="results" summary="This table contains the search results for schedule of classes.">
  <caption>
  Schedule of Classes Search Results
  </caption>
  <thead>
    <tr>
      <th scope="col">Course</th>
      <th scope="col">Code</th>
      <th scope="col">Section</th>
      <th scope="col">Title</th>
      <th scope="col">Day &amp; Time </th>
      <th scope="col">Dates</th>
      <th scope="col">Bldg &amp; Rm </th>
      <th scope="col">Instructor</th>
      <th scope="col">Seats Avail </th>
      <th scope="col">Comments</th>
    </tr>
  </thead>
  <tbody>
  	<%while(result.next()){%>
    <tr>
      <td><a href=<%="\"CourseDetails.jsp?Id=" + result.getString(2) + "\""%>><%=result.getString(1)%></a></td>
      <td><%=result.getString(2)%></td>
      <td><%=result.getString(3)%></td>
      <td><%=result.getString(4)%></td>
      <td><%=result.getString(5)%></td>
      <td><%=result.getString(6)%></td>
      <td><%=result.getString(7)%></td>
      <td><%=result.getString(8)%></td>
      <td><%=result.getString(9)%></td>
      <td><%=result.getString(10)%></td>
    </tr>
    <%}%>
 </tbody>
</table>
</form>
</div>
</div>
</body>
</html>