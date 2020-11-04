<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/Schedule">
		<html>
			<head>
				<title>Results</title>
			</head>
			<body>
				<table>
					<tr style="background-color:gray;">
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
