package com.ProjectController;

public class ProjectBean {
	
	private String semester;
	private String department;
	private String discipline;
	private String division;
	private String cNumber;
	private String days;
	private String timeAB;
	private String time;
	private String instructor;
	private String uG;
	
	public ProjectBean(){}
	
	public ProjectBean(String semester, String department, String discipline, String division, String cNumber, String days, String timeAB, String time, String instructor, String uG){
		this.semester = semester;
		this.department = department;
		this.discipline = discipline;
		this.division = division;
		this.cNumber = cNumber;
		this.days = days;
		this.timeAB = timeAB;
		this.time = time;
		this.instructor = instructor;
		this.setuG(uG);
	}
	
	public String getSemester() {
		return semester;
	}
	public void setSemester(String semester) {
		this.semester = semester;
	}
	public String getDepartment() {
		return department;
	}
	public void setDepartment(String department) {
		this.department = department;
	}
	public String getDiscipline() {
		return discipline;
	}
	public void setDiscipline(String discipline) {
		this.discipline = discipline;
	}
	public String getdivision() {
		return division;
	}
	public void setdivision(String division) {
		this.division = division;
	}
	public String getcNumber() {
		return cNumber;
	}
	public void setcNumber(String cNumber) {
		this.cNumber = cNumber;
	}
	public String getDays() {
		return days;
	}
	public void setDays(String days) {
		this.days = days;
	}
	public String getTimeAB() {
		return timeAB;
	}
	public void setTimeAB(String timeAB) {
		this.timeAB = timeAB;
	}
	public String getTime() {
		return time;
	}
	public void setTime(String time) {
		this.time = time;
	}
	public String getInstructor() {
		return instructor;
	}
	public void setInstructor(String instructor) {
		this.instructor = instructor;
	}
	
	public String getuG() {
		return uG;
	}

	public void setuG(String uG) {
		this.uG = uG;
	}

}
