package com.ProjectController;
import java.sql.*;

public class ProjectDAC {
	
	 private Connection connect() {
		
		Connection conn = null;
		String url = "jdbc:oracle:thin:@localhost:1521:XE";
		String uName = "CIS4160";
		String uPass = "CIS4160";
		
		try {
			Class.forName("oracle.jdbc.OracleDriver");
			conn = DriverManager.getConnection(url, uName, uPass);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return conn;
	}
	
	public ResultSet runQuery(String theQuery){
		
		Connection conn = connect();
		Statement statement = null;
		ResultSet result = null;
		try {
			statement = conn.createStatement();
			result = statement.executeQuery(theQuery);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return result;
	}
	
	
	public boolean evalSearch(String semester, String dept, String discipline, String division, String cNumber, String days, String timeAB, String time, String instructor){
		
		boolean result = false;
		
		if((semester != null)&&((!dept.equals("00"))||(!discipline.equals("00"))||(!cNumber.equals(""))||(!days.equals("00"))||(!time.equals("00"))||(!instructor.equals("")))){
			result = true;
		}else{
			result = false;
		}
		
		return result;
	}
	
	private String buildWhere(String semester, String dept, String discipline, String division, String cNumber, String days, String timeAB, String time, String instructor){
		
		String part3 = "WHERE COURSE_SR.COURSENUMBER = CRS_SEC_SR.CRS_NUM AND COURSE_SR.DISCIPLINE = CRS_SEC_SR.DISC AND DISCIPLINE_SR.DISC_ABBREVIATION = CRS_SEC_SR.DISC AND TITLE IS NOT NULL AND ";
		
		String semChunk = semester.substring(0,4);
		
		//Resolve Semester	
		if(semChunk.equals("Summ")){
			if(semester.substring(6,8).equals("01")){
				part3 += "START_DATE = '03-JUN-13' AND END_DATE = '11-JUL-13' ";
			}else if(semester.substring(6,8).equals("02")){
				part3 += "START_DATE = '15-JUL-13' AND END_DATE = '15-AUG-13' ";
			}else{
				part3 += "SEMESTER LIKE 'summ%' ";
			}
		}else if(semChunk.equals("Fall")){
			part3 += "SEMESTER LIKE 'fall%' ";
		}else if(semChunk.equals("Spri")){
			part3 += "SEMESTER LIKE 'spri%' ";
		}else if(semChunk.equals("Janu")){
			part3 += "SEMESTER LIKE 'janu%' ";
		}
			
		//Resolve department
		if(!dept.equals("00")){
			part3 += "AND DISCIPLINE_SR.DISCIPLINE_NAME = '"+dept+"' ";
		}
		
		//Resolve discipline
		if(!discipline.equals("00")){
			part3 += "AND DISC_ABBREVIATION = '"+discipline+"' ";
		}
			
		//Resolve grad of undergrad
		if(division != null){
			part3 += "AND D_E_G = '"+division+"' ";
		}
			
		//Resolve course number
		if(!cNumber.equals("")){
			part3 += "AND CRS_NUM = '"+cNumber+"' ";
		}
			
		//Resolve days
		if(!days.equals("00")){
			part3 += "AND MEETING_DAYS = '"+days+"' ";
		}
			
		//Resolve time
		if(!timeAB.equals("00")){
				
			String ampm = time.substring(5,7);
			String hour = time.substring(0,2);
				
			System.out.println(ampm);
			System.out.println(hour);
				
			if(timeAB.equals("before")){
				if(ampm.equals("AM")){
					part3 += "AND substr(START_TIME, 1,2) < '"+hour+"' AND AM_PM = 'AM' ";
				}
				if(hour.equals("12")){
					part3 += "AND substr(start_time, 1,2) >='01' And AM_PM = 'AM' ";
				} 
				if(ampm.equals("PM")){
					part3 += "AND substr(START_TIME, 1,2) <='11' AND AM_PM = 'AM' or substr(START_TIME, 1,2) = '12' and AM_PM = 'PM' OR substr(START_TIME, 1,2) < '"+hour+"' and AM_PM = 'PM' ";
				}
			}else if(timeAB.equals("after")){
				if((ampm.equals("PM"))&&(!hour.equals("12"))){
					part3 += "AND substr(START_TIME, 1,2) >= '"+hour+"' AND AM_PM = 'PM' ";
				}
				if((hour.equals("12"))&&(ampm.equals("PM"))){
					part3 += "AND substr(start_time, 1,2) >= '01' And AM_PM = 'PM' AND substr(start_time, 1,2) <= 12 AND AM_PM = 'PM' ";
				}
				if((!hour.equals("12"))&&(ampm.equals("AM"))){
					part3 += "AND substr(START_TIME, 1,2) <='11' AND AM_PM = 'PM' or substr(START_TIME, 1,2) = '12' and AM_PM = 'PM' OR substr(START_TIME, 1,2) >='"+hour+"' and AM_PM = 'AM' ";
				}
			}else if(timeAB.equals("around")){
				part3 += "AND substr(START_TIME, 1,2) = '"+hour+"' ";
			}
		}
			
		if(!instructor.equals("")){
			
			char begin = instructor.charAt(0);
			CharSequence rest = instructor.subSequence(1, instructor.length());
			
			part3 += "AND (SUBSTR(INSTRUCTOR_LNAME, 1,1) LIKE UPPER('"+begin+"') OR SUBSTR(INSTRUCTOR_LNAME, 1,1) LIKE UPPER('"+begin+"')) AND (INSTRUCTOR_LNAME LIKE UPPER('%"+rest+"%') OR INSTRUCTOR_LNAME LIKE LOWER('%"+rest+"%')) ";
		}
				
		return part3;
	}
	
	public String dispQuery(String semester, String dept, String discipline, String division, String cNumber, String days, String timeAB, String time, String instructor){
		
		String part1 = "SELECT semester, concat(DISC_ABBREVIATION, concat(' ', CRS_NUM)), TITLE, CRS_CD, CRS_SEC, discipline_name, concat(TO_CHAR(START_DATE, 'MM/DD/YYYY'), concat(' - ', TO_CHAR(END_DATE, 'MM/DD/YYYY'))), SEATS_AVAIL, concat(MEETING_DAYS, concat(' ', concat(START_TIME, concat(AM_PM, concat(' ', concat(STOP_TIME, AM_PM)))))), concat(BUILDING, concat(' ', RM)), INSTRUCTOR_LNAME, NVL(CREDITHOUR, 'Unavailable'), DESCRIPTION, NVL(CRS_COMMENTS1, 'Unavailable'), NVL(PREREQ, 'Prerequisite: None') ";
        String part2 = "FROM COURSE_SR NATURAL JOIN CRS_SEC_SR NATURAL JOIN DISCIPLINE_SR natural join CRS_COMMENTS_SR ";
        
        //String semester, String dept, String discipline, String division, String cNumber, String days, String timeAB, String time, String instructor
        String query = part1 + part2 + buildWhere(semester, dept, discipline, division, cNumber, days, timeAB, time, instructor);
		
        return query;
	}
	
	public String buildSearch(String semester, String dept, String discipline, String division, String cNumber, String days, String timeAB, String time, String instructor){
		
		String part1 = "SELECT concat(DISC_ABBREVIATION, concat(' ', CRS_NUM)), CRS_CD, CRS_SEC, TITLE, concat(MEETING_DAYS, concat(' ', concat(START_TIME, concat(AM_PM, concat(' - ', concat(STOP_TIME, AM_PM)))))), concat(TO_CHAR(START_DATE, 'MM/DD/YYYY'), concat(' - ', TO_CHAR(END_DATE, 'MM/DD/YYYY'))), concat(BUILDING, concat(' ', RM)), INSTRUCTOR_LNAME, SEATS_AVAIL, NVL(CREDITHOUR, '-----')";
		String part2 = "FROM COURSE_SR NATURAL JOIN CRS_SEC_SR NATURAL JOIN DISCIPLINE_SR ";
		
		String query = part1+part2+buildWhere(semester, dept, discipline, division, cNumber, days, timeAB, time, instructor);
		System.out.println(query);
		return query;
	}
	
	public static void main(String[] args) {
		//ProjectDAC dac = new ProjectDAC();
		//String conn = dac.buildSearch("Spring", "ART", "00", "D", "", "S", "00", "00", "klein");
		//System.out.print(conn);
		//"Spring", "ART", "00", "D", "", "S", "00", "00", ""
	}

}
