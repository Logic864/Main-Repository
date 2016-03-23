<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@page language="java" session="true" %>
<%@page import = "java.sql.*" import = "com.ProjectController.*" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<meta name="description" content="" />
<meta name="keywords" content="" />
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<link REL="icon" href="http://www.baruch.cuny.edu/favicon.ico">
<link rel="stylesheet" type="text/css" href="baruch_interior.css" />
<link rel="stylesheet" type="text/css" href="http://www.baruch.cuny.edu/css/application.css" />
<link href="scheduler.css" rel="stylesheet" type="text/css" />
<%//Use scriptlet to handle query execution

//Create and initialize variables for the query, controller class, and search result
String query = null; ProjectDAC displayDAC = new ProjectDAC(); ResultSet result = null; String resID = null;

//Get the bean from the session
ProjectBean mySearch = (ProjectBean) session.getAttribute("searchBean");
query = displayDAC.dispQuery(mySearch.getSemester(), mySearch.getDepartment(), mySearch.getDiscipline(), mySearch.getdivision(), mySearch.getcNumber(), mySearch.getDays(), mySearch.getTimeAB(), mySearch.getTime(), mySearch.getInstructor());  
query += "AND CRS_CD = '"+request.getParameter("Id")+"' ";
System.out.println(query);
result = displayDAC.runQuery(query);%>
<title>Course Description</title>
</head>
<body>
<div id="wrapper">
<div id="banner"><a href="http://www.baruch.cuny.edu"><img src="http://www.baruch.cuny.edu/images/logo_baruch.gif" alt="Baruch College" name="logo" width="201" height="68" border="0" id="logo" /></a></div>
<div id="main">
<table id="details" summary="This table contains details about each course.">
<caption>
Schedule of Classes Course Details 
</caption>
<%while(result.next()){%>  
  <tr>
    <th scope="row">Semester:</th>
    <td><%=result.getString(1)%></td>
  </tr>
  <tr>
    <th scope="row">Course - Title:</th>
    <td><%=result.getString(2)%> - <%=result.getString(3)%></td>
  </tr>
  <tr>
    <th scope="row">Code:</th>
    <td><%=result.getString(4)%></td>
  </tr>
  <tr>
    <th scope="row">Section:</th>
    <td><%=result.getString(5)%></td>
  </tr>
  <tr>
    <th scope="row">Department:</th>
    <td><%=result.getString(6)%></td>
  </tr>
  <tr>
    <th scope="row">Division:</th>
    <td>${searchBean.uG}</td>
  </tr>
  <tr>
    <th scope="row">Dates:</th>
    <td><%=result.getString(7)%></td>
  </tr>
  <tr>
    <th scope="row">Seats Available:</th>
    <td><%=result.getString(8)%></td>
  </tr>
  <tr>
    <th scope="row">Day &amp; Time, Building &amp; Room, Instructor: </th>
    <td><%=result.getString(9)%>, <%=result.getString(10)%>, <%=result.getString(11)%> </td>
  </tr>
  <tr>
    <th scope="row">Credit Hours: </th>
    <td><%=result.getString(12)%></td>
  </tr>
  <tr>
    <th scope="row">Description:</th>
    <td><p><%=result.getString(14)%></p>
    <p><em>This course may not be taken with the Pass/Fail option.</em></td>
  </tr>
  <tr>
    <th scope="row">Course Comments: </th>
    <td><%=result.getString(13)%></td>
  </tr>
  <tr>
    <th scope="row">Pre-requisite:</th>
    <td><%=result.getString(15)%></td>
  </tr>
<%}%>
</table>
</div>
</div>
</body>
</html>