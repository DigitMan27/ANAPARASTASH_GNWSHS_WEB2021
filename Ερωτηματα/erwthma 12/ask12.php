<?php
	if($_POST['call']=='sub'){
		$file = $_POST["path1"];
		$schema = $_POST["path2"];
		$filter = $_POST['days'];
		file2table($file,$schema,$filter);
	}else{
		$file = $_POST["path1"];
		add2table($file);
	}

	function file2table($filename,$schema,$day_q){
		//echo $file;
		$xml = new DOMDocument();
		$xml->preserveWhiteSpace = false;
		$xml->load($filename);
		if(!$xml->schemaValidate($schema)){
			echo "Validation Error";
			exit;
		}
		$day_arr = explode(',', $day_q);

		$table_head = '<tr><th>Lesson</th><th>Professor</th><th>Day</th></tr>';
		$count = 1;
		$x = $xml->documentElement;
		foreach ($x->childNodes as $data) {
			$day = $data->getElementsByTagName('Day')->item(0)->nodeValue;
			if(in_array($day,$day_arr)){
				$lesson = $data->getElementsByTagName('Title')->item(0)->nodeValue;
				if(is_object($data->getElementsByTagName('Professor')->item(0))){
					$professor = $data->getElementsByTagName('Professor')->item(0)->nodeValue;
				}else{
					$professor = '';
				}
				//$day = $data->getElementsByTagName('Day')->item(0)->nodeValue;
				$table_head .='<tr><td align="center">'.$lesson.'</td><td align="center">'.$professor.'</td><td align="center">'.$day.'</td></tr>';
			}
		}
			//$table_head.'</table>';
		echo $table_head;
	}

	function add2table($filename){
		$xml = new DOMDocument();
		$xml->preserveWhiteSpace = false;
		$xml->load($filename);
		
		$title = $_POST['lesson'];
		$Prof = $_POST['Professor'];
		$day = $_POST['day'];

		$parent = $xml->firstChild; // access schedule node
		//Eisagwgh ma8hmatos
		$new_lesson = $xml->createElement("Lesson");
		//title
		$new_title = $xml->createElement("Title");
		$lesson_title = $xml->createTextNode($title);
		//Lecture
		$new_lect = $xml->createElement("Lecture");
		$new_day = $xml->createElement("Day");
		$new_day_val = $xml->createTextNode($day);
		$new_time = $xml->createElement("Time");
		$new_time_val = $xml->createTextNode("10:00-13:00"); // bazw mia tuxaia afou den to exw san pedio
		//Append childs
		//For title tag
		$new_lesson->appendChild($new_title);
		$new_title->appendChild($lesson_title);
		//For lecture tag
		$new_lesson->appendChild($new_lect);
		$new_lect->appendChild($new_day);
		$new_day->appendChild($new_day_val);
		$new_lect->appendChild($new_time);
		$new_time->appendChild($new_time_val);
		//Professor
		if($Prof!=''){
			$new_prof = $xml->createElement("Professor");
			$new_prof_val = $xml->createTextNode($Prof);

			$new_lesson->appendChild($new_prof);
			$new_prof->appendChild($new_prof_val);
		}
		//root
		$parent->appendChild($new_lesson);
		$xml->formatOutput = true;
		
		file_put_contents($filename, $xml->saveXML());
	}
?>