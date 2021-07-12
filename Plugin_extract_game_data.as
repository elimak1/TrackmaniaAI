/*
Copy this file to openplanet scripts folder, more info about openplanet at https://openplanet.nl/
*/
#name "EGD"
#author "elimak"
#category "In Game"
// https://next.openplanet.nl/ShootMania/CSmScriptPlayer for ScriptAPI class members
void Main(){
	while(true){
		while(cast<CTrackManiaNetwork>(GetApp().Network).ClientManiaAppPlayground !is null) //This will replace <scripts> parts, it'll be active as long as the UI can be loaded
		{
			
			auto currentPlayground = cast<CSmArenaClient>(GetApp().CurrentPlayground);
			if(currentPlayground is null)
				{yield();continue;}//I don't yield at the begining or pending event will be cleared

			auto players = currentPlayground.GameTerminals;
			if(players.Length <= 0)
				{yield();continue;}

			auto game_terminal = cast<CGameTerminal>(players[0]);
			if(game_terminal is null)
				{yield();continue;}

			auto game_player = cast<CSmPlayer>(game_terminal.GUIPlayer);
			if(game_player is null)
				{yield();continue;}

			auto plr_api = cast<CSmScriptPlayer>(game_player.ScriptAPI); //All those leads to playerScriptApi to retrieve player speed
			if(plr_api is null)
				{yield();continue;}

			string speed = ""+plr_api.DisplaySpeed;
			string raceTime = ""+plr_api.CurrentRaceTime;
			uint checkpoint = game_player.CurrentStoppedRespawnLandmarkIndex;

			print(speed+";"+raceTime+";"+checkpoint);
			IO::File f("gameState.txt");
			f.Open(IO::FileMode::Write);
			f.WriteLine(speed+";"+raceTime+";"+checkpoint);
			f.Close();
			sleep(10);
		}
		
		
	}
}