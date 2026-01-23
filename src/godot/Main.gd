extends Node

enum GameState {
	MAIN_SCREEN,
	NAME_SCREEN,
	EXPLORE,
	PAUSE,
	BATTLE
}
var state = GameState.MAIN_SCREEN
func _ready():
	Set_State(GameState.MAIN_SCREEN)
	
func Set_State(updated_state):
	state=updated_state
	$main_screen.visible=state==GameState.MAIN_SCREEN
	$naming.visible=state==GameState.NAME_SCREEN
	$UI.visible=state==GameState.EXPLORE
	$pause_screen.visible=state==GameState.PAUSE
	$Battle_UI.visible=state==GameState.BATTLE
	$Battle.visible=state==GameState.BATTLE
