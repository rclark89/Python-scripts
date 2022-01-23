--Data source: https://ourworldindata.org/covid-deaths

SELECT *
FROM portfolio_project.dbo.covid_deaths
WHERE continent IS NOT NULL
ORDER BY 3,4

--SELECT *
--FROM portfolio_project.dbo.covid_vaccinations
--ORDER BY 3,4

--Select the data we want to use.
SELECT location, date, total_cases, new_cases, total_deaths, population
FROM portfolio_project.dbo.covid_deaths
WHERE continent IS NOT NULL
ORDER BY 1,2

--Examine total depths vs total cases
--Shows approx likelihood of dying from covid.
SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 AS death_percentage
FROM portfolio_project.dbo.covid_deaths
WHERE location LIKE '%states%'
ORDER BY 1,2

-- Examine total cases vs population
-- Shows % of population with covid.
SELECT location, date, population, total_cases, (total_cases/population*100) AS infected_percentage
FROM portfolio_project.dbo.covid_deaths
WHERE location LIKE '%states%'
ORDER BY 1,2

-- Looking at countries with highest infection rate compared to population
SELECT location, population, MAX(total_cases) as highest_infection_count, MAX((total_cases/NULLIF(population,0))*100) AS infected_percentage
FROM portfolio_project.dbo.covid_deaths
WHERE continent IS NOT NULL
--WHERE location LIKE '%states%'
GROUP BY location, population
ORDER BY infected_percentage DESC

-- Shows countries with highest death count per population
SELECT location, MAX(CAST(total_deaths AS int)) AS total_death_count
FROM portfolio_project.dbo.covid_deaths
WHERE continent IS NOT NULL
--WHERE location LIKE '%states%'
GROUP BY location
ORDER BY total_death_count DESC

-- Divide results by continent
-- Shows countries with highest death count per population

SELECT continent, MAX(CAST(total_deaths AS int)) AS total_death_count
FROM portfolio_project.dbo.covid_deaths
WHERE continent IS NOT NULL
--WHERE location LIKE '%states%'
GROUP BY continent
ORDER BY total_death_count DESC

-- Worldwide figures
SELECT SUM(new_cases) AS total_cases, SUM(CAST(new_deaths AS INT)) AS total_deaths, SUM(CAST(new_deaths AS INT))/SUM(new_cases)*100 AS death_percentage --total_cases, total_deaths, (total_deaths/total_cases)*100 AS death_percentage
FROM portfolio_project.dbo.covid_deaths
WHERE continent IS NOT NULL
--GROUP BY date
ORDER BY 1,2

-- Join death figs with vaccination figures
SELECT *
FROM portfolio_project.dbo.covid_deaths AS dea
JOIN portfolio_project.dbo.covid_vaccinations AS vac
ON dea.location = vac.location
AND dea.date = vac.date

-- Look at total pop vs vaccinations
-- Includes rolling total for new vaccinations

SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
SUM(CONVERT(bigint, vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS rolling_vaccine_count,

FROM portfolio_project.dbo.covid_deaths AS dea
JOIN portfolio_project.dbo.covid_vaccinations AS vac
ON dea.location = vac.location
AND dea.date = vac.date
WHERE dea.continent IS NOT NULL
ORDER BY 2,3

