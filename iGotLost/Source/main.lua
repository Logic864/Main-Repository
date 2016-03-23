-----------------------------------------------------------------------------------------
--
-- main.lua
--
-----------------------------------------------------------------------------------------

-- Your code here
physics = require("physics")
physics.start()

local attempts = 0
local contents
display.setStatusBar( display.HiddenStatusBar )  -- hides status bar
local w = display.contentWidth
local h = display.contentHeight
local result = 0
local ding = audio.loadSound("ding.wav")
local music  = audio.loadStream("elevator.wav")
local mainChannel = audio.play(music, {channel = 1, loops = -1})
local mymap = native.newMapView( display.contentCenterX, display.contentCenterY, w, h )
mymap.isVisible=false
local background = display.newImage( "map.jpg")
background.x=w
background.y=0


local function bReverse()
	transition.moveTo(background, {x=w, y=0, time=60000, onComplete=bForward})
end

function bForward()
	transition.moveTo(background, {x=0, y=h, time=60000, onComplete=bReverse})
end

bForward(background)

local rectangle = display.newRect(w/2, h/2, 275, 500)
rectangle.alpha = 0.7

local welcomeText = display.newText("Welcome to",w/2,100,Arial, 30)
welcomeText:setFillColor( 0, 0.5, 1 )
local welcome2Text = display.newText("iGotLost!",w/2,140,Arial, 30)
welcome2Text:setFillColor( 0, 0.5, 1 )


local mapLocationButton = display.newRoundedRect( w/2,220, 180, 40,  4)
mapLocationButton: setFillColor ( 0, 0.5, 1 )
local mapText = display.newText("Map My Location",w/2,220,Arial, 20)

local findCarButton = display.newRoundedRect( w/2,280, 180, 40,  4)
findCarButton: setFillColor ( 0, 0.5, 1 )
local findText = display.newText("Find My Car",w/2,280,Arial, 20)

local exitButton = display.newRoundedRect( w/2,250, 180, 40,  4)
exitButton: setFillColor ( 0, 0.5, 1 )
local exitText = display.newText("Exit", w/2,250,Arial, 20)
exitButton.isVisible = false
exitText.isVisible = false
local wheel = display.newImage("wheel.png", w, h)
wheel.isVisible=false

local confused= display.newImage( "confused.png",w/2,400)

local function exitApp ( event )
	native.requestExit()
end

local function findCar( event )
	local path = system.pathForFile( "carlocation.txt", system.DocumentsDirectory )
	local file, errorString = io.open( path, "r" )
	welcomeText.text="Working..."
	welcome2Text.isVisible=false
	if not file then
    -- Error occurred; output the cause
		native.showAlert("Oops!", "the file wasn't found", {"OK"})
	else
    -- Output lines
		contents = file:read("*a")
    -- Close the file handle
    io.close( file )
	end
	file = nil
	
	local current = mymap:getUserLocation()
	
	if current.errorCode or current.latitude == nil or current.longitude == nil then
        --locationText.text = currentLocation.errorMessage
		attempts = attempts + 1

        if ( attempts > 10 ) then
            native.showAlert( "No GPS Signal", "Can't sync with GPS.", { "OK" } )
			attempts = 0
        else
            timer.performWithDelay( 1000, findCar )
        end
    else
		local currentLatitude = current.latitude
		local currentLongitude = current.longitude
		local fromLoc = currentLatitude..","..currentLongitude
		local toLoc = contents
		--test = display.newText(toLoc, display.contentCenterX, display.contentCenterY-50)
		--test2 = display.newText(fromLoc, display.contentCenterX, display.contentCenterY+50)
		url = "https://www.google.com/maps/dir/"..fromLoc.."/"..toLoc.."/@"..fromLoc
		system.openURL( url ) 
	end
end

local function map( event )
	local current = mymap:getUserLocation()
	
	if current.errorCode or current.latitude == nil or current.longitude == nil then
		attempts = attempts + 1
		welcomeText.text="Working..."
		welcome2Text.isVisible=false
		mapLocationButton.isVisible=false
		mapText.isVisible=false
		findCarButton.isVisible=false
		findText.isVisible=false
		wheel.isVisible=true
		wheel:rotate(-360)
        if ( attempts > 10 ) then
			welcomeText.text="Welcome to"
			welcome2Text.isVisible=true
			mapLocationButton.isVisible=true
			mapText.isVisible=true
			findCarButton.isVisible=true
			findText.isVisible=true
			exitButton.isVisible=false
			exitText.isVisible=false
			confused.isVisible=true
            native.showAlert( "No GPS Signal", "Can't sync with GPS.", { "OK" } )
			attempts = 0
        else
            timer.performWithDelay( 1000, map )
        end
    else
        local path = system.pathForFile( "carlocation.txt", system.DocumentsDirectory )
		local file, errorString = io.open( path, "w" )

		if not file then
    -- Error occurred; output the cause
			native.showAlert("Oops!", "the file wasn't created", {"OK"})
		else
    -- Write data to file
			file:write( current.latitude, ",", current.longitude )
    -- Close the file handle
			io.close( file )
		end
		audio.play(ding)
		welcomeText.text="Coordinates Saved!"
		welcomeText.size=25
		welcome2Text.text="Feel free to go about your existence"
		welcome2Text.size=15
		welcome2Text.isVisible=true
		exitButton.isVisible=true
		exitText.isVisible=true
		mapLocationButton.isVisible=false
		mapText.isVisible=false
		findCarButton.isVisible=false
		findText.isVisible=false
		confused.isVisible=false
		okay= display.newImage( "okay.png",w/2,400)
    end
end

mapLocationButton:addEventListener("tap", map)
findCarButton:addEventListener("tap", findCar)
exitButton:addEventListener("tap", exitApp)