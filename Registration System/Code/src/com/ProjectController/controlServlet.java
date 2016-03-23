package com.ProjectController;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 * Servlet implementation class controlServlet
 */
@WebServlet("/controlServlet")
public class controlServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public controlServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		
		//Create instance of controller class to access functions
		ProjectDAC mainDAC = new ProjectDAC();
		//Create variable to consolidate grad or undergrad
		String division = null;
		
		//Get all parameters from the search form
		String semester = request.getParameter("semester");
		String department = request.getParameter("department");
		String discipline = request.getParameter("discipline");
		String grad = request.getParameter("div_grad");
		String uGrad = request.getParameter("div_undr");
		String cNumber = request.getParameter("number");
		String days = request.getParameter("days");
		String timeAB = request.getParameter("time_a_b");
		String time = request.getParameter("time");
		String instructor = request.getParameter("prof");
		
		//Determine what division should be equal to
		String uG = null;
		if (grad != null){
			division = grad;
			uG = "Graduate";
		}else if(uGrad != null){
			division = uGrad;
			uG = "Undergraduate";
		}else{
			division = null;
			uG = "Not Selected";
		}
		
		//Send search parameters to the controller to ensure they are correct
		if(mainDAC.evalSearch(semester, department, discipline, division, cNumber, days, timeAB, time, instructor) == true){
			//Create an instance of Project bean and put it into the session before going to the results page
			ProjectBean searchBean = new ProjectBean(semester, department, discipline, division, cNumber, days, timeAB, time, instructor, uG);
			HttpSession session = request.getSession();
			session.setAttribute("searchBean", searchBean);
			RequestDispatcher dispatcher = request.getRequestDispatcher("SearchResults.jsp");
			dispatcher.forward(request, response);
		}else{
			response.sendRedirect("SearchError.jsp");
		}
	}	
	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//doGet(request, response);
		
	}

}
