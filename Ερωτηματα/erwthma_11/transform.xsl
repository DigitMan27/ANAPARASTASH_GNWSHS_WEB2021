<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:variable name="DaysOfWeek">
		<Week>
			<Day id="Monday">1</Day>
			<Day id="Tuesday">2</Day>
			<Day id="Wednesday">3</Day>
			<Day id="Thursday">4</Day>
			<Day id="Friday">5</Day>
		</Week>
	</xsl:variable>
	<xsl:variable name="x">0</xsl:variable>
	<xsl:template match="/Schedule">
		<html>
			<head>
				<title>Results</title>
			</head>
			<body>
				<table>
					<tr>
						<th>Lesson</th>
						<th>Professor</th>
						<th>Day</th>
					</tr>
					<xsl:for-each select="//Lecture">
						<xsl:choose>
							<xsl:when test="Day/text()='Monday'">
								<tr style="background-color:#D241D5">
									<td><xsl:value-of select="../Title"/></td>
									<td><xsl:value-of select="../Professor"/></td>
									<td><xsl:value-of select="Day"/></td>
								</tr>
							</xsl:when>
						</xsl:choose>
					</xsl:for-each>
					<xsl:for-each select="//Lecture">
						<xsl:choose>
							<xsl:when test="Day/text()='Tuesday'">
								<tr style="background-color:#D2BC36">
									<td><xsl:value-of select="../Title"/></td>
									<td><xsl:value-of select="../Professor"/></td>
									<td><xsl:value-of select="Day"/></td>
								</tr>
							</xsl:when>
						</xsl:choose>
					</xsl:for-each>
					<xsl:for-each select="//Lecture">
						<xsl:choose>
							<xsl:when test="Day/text()='Wednesday'">
								<tr style="background-color:#64BCAA">
									<td><xsl:value-of select="../Title"/></td>
									<td><xsl:value-of select="../Professor"/></td>
									<td><xsl:value-of select="Day"/></td>
								</tr>
							</xsl:when>
						</xsl:choose>
					</xsl:for-each>
					<xsl:for-each select="//Lecture">
						<xsl:choose>
							<xsl:when test="Day/text()='Thursday'">
								<tr style="background-color:#64BC50">
									<td><xsl:value-of select="../Title"/></td>
									<td><xsl:value-of select="../Professor"/></td>
									<td><xsl:value-of select="Day"/></td>
								</tr>
							</xsl:when>
						</xsl:choose>
					</xsl:for-each>
					<xsl:for-each select="//Lecture">
						<xsl:choose>
							<xsl:when test="Day/text()='Friday'">
								<tr style="background-color:#FE6550">
									<td><xsl:value-of select="../Title"/></td>
									<td><xsl:value-of select="../Professor"/></td>
									<td><xsl:value-of select="Day"/></td>
								</tr>
							</xsl:when>
						</xsl:choose>
					</xsl:for-each>
				</table>
			</body>
		</html>
		
	</xsl:template>
</xsl:stylesheet>

<!--
<xsl:variable name="curr_day"><xsl:value-of select="Day"/></xsl:variable>
						<xsl:sort select="$DaysOfWeek/Week/Day"/>
						 <xsl:text>value=</xsl:text>
						<xsl:value-of select="$curr_day"/> 
						<tr>
							<td><xsl:value-of select="../Title"/></td>
							<td><xsl:value-of select="../Professor"/></td>
							<td>
								<xsl:choose>
									<xsl:when test="Day/text()='Friday' or Day/text()='Thursday' or Day/text()='Wednesday' or Day/text()='Tuesday' or Day/text()='Monday'">
										<xsl:value-of select="$DaysOfWeek/Week/Day[@id=$curr_day]/text()"/>
									</xsl:when>
									<xsl:otherwise>  Isws n mhn xreiazetai 
										<xsl:value-of select="Day"/>
									</xsl:otherwise>
								</xsl:choose>
							</td>
						</tr> 
-->
