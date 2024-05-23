<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <head>
    <title>Résultat mensuel</title>
    <!-- CDN Bootstrap - CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous" />
    <!-- fichier style.css -->
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div classs="container">
      <h2 class="center">Résultat <xsl:value-of select="MonthResult/Year" />-<xsl:value-of select="MonthResult/Month" /></h2>
        <xsl:choose>
          <xsl:when test="MonthResult/Delta &gt; 0">
            <p class="green center">
              CA : <b><xsl:value-of select="MonthResult/Ca" /> &#8364; </b> -
              hours : <b><xsl:value-of select="MonthResult/Hours" /> h</b>
              (hsup : <b><xsl:value-of select="MonthResult/HSup" /> h</b>) -
              prime : <b><xsl:value-of select="MonthResult/Prime" /> &#8364;</b> (&#x394; = <xsl:value-of select="MonthResult/Delta" />)
            </p>
          </xsl:when>
          <xsl:otherwise>
            <p class="red center">
              CA : <b><xsl:value-of select="MonthResult/Ca" /> &#8364; </b> -
              hours : <b><xsl:value-of select="MonthResult/Hours" /> h</b>
              (hsup : <b><xsl:value-of select="MonthResult/HSup" /> h</b>) -
              prime : <b><xsl:value-of select="MonthResult/Prime" /> &#8364;</b> (&#x394; = <xsl:value-of select="MonthResult/Delta" />)
            </p>
          </xsl:otherwise>
        </xsl:choose>
    </div>
    <div class="row">
      <div class="col">
        <div class="container">
          <table class="table">
            <thead>
              <tr class="table-primary">
                <th scope="col" class="center">Jour</th>
                <th scope="col" class="center">CA</th>
                <th scope="col" class="center">nb heures</th>
                <th scope="col" class="center">h sup</th>
                <th scope="col" class="center">moyenne</th>
                <th scope="col" class="center">commentaire</th>
              </tr>
            </thead>
            <tbody>
              <xsl:for-each select="MonthResult/Results/DayResult">
                <xsl:choose>
                  <xsl:when test="Average &gt; 25">
                    <tr>
                      <td scope="row" class="my center"><xsl:value-of select="Date"/></td>
                      <td class="my green right"><xsl:value-of select="Ca"/></td>
                      <td class="my green center"><xsl:value-of select="Hours"/></td>
                      <td class="my green center"><xsl:value-of select="HSup"/></td>
                      <td class="my green center"><xsl:value-of select="Average"/></td>
                      <td class="my green right"><xsl:value-of select="Comment"/></td>
                    </tr>              </xsl:when>
                  <xsl:otherwise>
                    <tr>
                      <td scope="row" class="my center"><xsl:value-of select="Date"/></td>
                      <td class="my red right"><xsl:value-of select="Ca"/></td>
                      <td class="my red center"><xsl:value-of select="Hours"/></td>
                      <td class="my red center"><xsl:value-of select="HSup"/></td>
                      <td class="my red center"><xsl:value-of select="Average"/></td>
                      <td class="my red right"><xsl:value-of select="Comment"/></td>
                    </tr>
                  </xsl:otherwise>
                </xsl:choose>
              </xsl:for-each>
            </tbody>
          </table>
        </div>
      </div>
      <div class="col">
        <img src="suivi_results.png" alt="graphe suivi des resultats"/>
      </div>
    </div>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>
