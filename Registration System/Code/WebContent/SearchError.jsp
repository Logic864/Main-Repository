<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
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
<%String query = null; ProjectDAC searchDAC = new ProjectDAC(); ResultSet result = null;%>
<title>Whoops!</title>
</head>
<body>
<div id="wrapper">
<div id="banner"><a href="http://www.baruch.cuny.edu"><img src="http://www.baruch.cuny.edu/images/logo_baruch.gif" alt="Baruch College" name="logo" width="201" height="68" border="0" id="logo" /></a></div>
<div id="main">
<form method="get" action="controlServlet">
	 <div align="center">
      <p class="errormsg"><b><font color="#FF0000">You must select a semester and either a discipine, course number, day, time, and/or instructor.</font></b> </p>
	  <p class="errormsg"><b><font color="#FF0000">Both drop-downs for time must either be blank or contain a value.</font></b> </p>
      <p>Enter the professor's name, discipline, course number and/or days you wish to search.</p>
      <table id="search" summary="This table contains search options for the schedule of classes.">
       <caption>Schedule of Classes Search&nbsp; - <a href="schedulesearcherror.html">ERROR</a></caption>
	  <tbody>
        <tr>
        <%query = "select semester_name, ' ', to_char(start_date, 'mm/dd/yyyy'), ' to ', to_char(end_date, 'mm/dd/yyyy') from SEMESTER_SR";
          result = searchDAC.runQuery(query);%>
          <th><label for="semester">Semester:</label></th>
          <td><select id="semester" name="semester">
          	<option value="" disabled selected>Session</option>
          	<%while(result.next()){%>
			<option><%=result.getString(1)%><%=result.getString(2)%><%=result.getString(3)%><%=result.getString(4)%><%=result.getString(5)%></option>
			<%}%>
           </select></td>
        </tr>
        <tr>
        <%query = "select discipline_name from DISCIPLINE_SR order by DISCIPLINE_NAME asc";
          result = searchDAC.runQuery(query);%>
          <th>Dept:</th>
          <td><select name="department" size="1">
			<option value="00">Select All</option>
			<%while(result.next()){%>
			<option><%=result.getString(1)%></option>
			<%}%>
			</select></td>
        </tr>
        <tr>
        <%query = "select disc_abbreviation from DISCIPLINE_SR order by disc_abbreviation asc";
          result = searchDAC.runQuery(query);%>
          <th>Discipline:</th>
          <td><select name="discipline" size="1">
            <option value="00">Select All</option>
            <%while(result.next()){%>
			<option><%=result.getString(1)%></option>
			<%}%>
			</select></td>
        </tr>
        <tr>
          <th>Division</th>
          <td>
            <label for="undergraduate">Undergraduate </label><input type="checkbox" id="undergraduate" value="D" name="div_undr">
            <br>
            <label for="graduate">Graduate</label><input type="checkbox" id="gradaute" value="G" name="div_grad">
          </td>
        </tr>
        <tr>
          <th><label for="number">Course number:</label></th>
          <td><input id="number" size="10" name="number" maxlength="5" type="text"></td>
        </tr>
        <tr>
        <%query = "select distinct meeting_days from CRS_SEC_SR order by MEETING_DAYS asc";
          result = searchDAC.runQuery(query);%>
          <th><label for="days">Days:</label></th>
          <td><select id="days" name="days">
              <option value="00">Select	All </option>
              <%while(result.next()){%>
			  <option><%=result.getString(1)%></option>
			  <%}%>
          </select></td>
        </tr>
        <tr>
        <%query = "select distinct start_time, am_pm from CRS_SEC_SR where substr(START_TIME, 4,5) = '00' order by am_pm asc";
          result = searchDAC.runQuery(query);%>
          <th><label for="time">Time:</label></th>
          <td><select id="time" name="time_a_b">
              <option value="00">Select	All </option>
              <option>before </option>
              <option>after </option>
              <option>around </option>
            </select>
            <select name="time">
              <option value="00">Select	All </option>
              <%while(result.next()){%>
			  <option><%=result.getString(1)%><%=result.getString(2)%></option>
			  <%}%>
            </select>          </td>
        </tr>
        <tr>
          <th><label for="instructor">Instructor:</label></th>
          <td><input id="instructor" size="30" name="prof" type="text"></td>
        </tr>
      </tbody>
      </table>
    </div>
    <p align="center">
      <input value="Start Search" type="submit">
   </p>
 
</form>
</div>
</div>
</body>
</html>